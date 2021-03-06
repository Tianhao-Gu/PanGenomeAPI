# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class PanGenomeAPI(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def search_orthologs_from_pangenome(self, params, context=None):
        """
        :param params: instance of type "SearchOrthologsFromPG" (num_found -
           optional field which when set informs that there is no need to
           perform full scan in order to count this value because it was
           already done before; please don't set this value with 0 or any
           guessed number if you didn't get right value previously.) ->
           structure: parameter "pangenome_ref" of String, parameter "query"
           of String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchOrthologsFromPGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "orthologs" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "orthologs" of list
           of type "OrthologsData" (OrthologFamily object: this object holds
           all data for a single ortholog family in a metagenome @optional
           type function md5 protein_translation) -> structure: parameter
           "id" of String, parameter "type" of String, parameter "function"
           of String, parameter "md5" of String, parameter
           "protein_translation" of String, parameter "orthologs" of list of
           tuple of size 3: String, Double, String, parameter "num_found" of
           Long
        """
        return self._client.call_method(
            'PanGenomeAPI.search_orthologs_from_pangenome',
            [params], self._service_ver, context)

    def search_families_from_comparison_genome(self, params, context=None):
        """
        :param params: instance of type "SearchFamiliesFromCG" -> structure:
           parameter "comparison_genome_ref" of String, parameter "query" of
           String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchFamiliesFromCGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "families" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "families" of list of
           type "GenomeComparisonFamily" (GenomeComparisonFamily object: this
           object holds information about a protein family across a set of
           genomes) -> structure: parameter "core" of Long, parameter
           "genome_features" of mapping from String to list of tuple of size
           3: type "Feature_id", list of Long, Double, parameter "id" of
           String, parameter "type" of String, parameter
           "protein_translation" of String, parameter "number_genomes" of
           Long, parameter "fraction_genomes" of Double, parameter
           "fraction_consistent_annotations" of Double, parameter
           "most_consistent_role" of String, parameter "num_found" of Long
        """
        return self._client.call_method(
            'PanGenomeAPI.search_families_from_comparison_genome',
            [params], self._service_ver, context)

    def search_functions_from_comparison_genome(self, params, context=None):
        """
        :param params: instance of type "SearchFunctionsFromCG" -> structure:
           parameter "comparison_genome_ref" of String, parameter "query" of
           String, parameter "sort_by" of list of type "column_sorting" ->
           tuple of size 2: parameter "column" of String, parameter
           "ascending" of type "boolean" (Indicates true or false values,
           false = 0, true = 1 @range [0,1]), parameter "start" of Long,
           parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchFunctionsFromCGResult" (num_found -
           number of all items found in query search (with only part of it
           returned in "functions" list).) -> structure: parameter "query" of
           String, parameter "start" of Long, parameter "functions" of list
           of type "GenomeComparisonFunction" (GenomeComparisonFunction
           object: this object holds information about a genome in a function
           across all genomes) -> structure: parameter "core" of Long,
           parameter "genome_features" of mapping from String to list of
           tuple of size 3: type "Feature_id", Long, Double, parameter "id"
           of String, parameter "reactions" of list of tuple of size 2: type
           "Reaction_id", String, parameter "subsystem" of String, parameter
           "primclass" of String, parameter "subclass" of String, parameter
           "number_genomes" of Long, parameter "fraction_genomes" of Double,
           parameter "fraction_consistent_families" of Double, parameter
           "most_consistent_family" of String, parameter "num_found" of Long
        """
        return self._client.call_method(
            'PanGenomeAPI.search_functions_from_comparison_genome',
            [params], self._service_ver, context)

    def search_comparison_genome_from_comparison_genome(self, params, context=None):
        """
        :param params: instance of type "SearchComparisonGenomesFromCG" ->
           structure: parameter "comparison_genome_ref" of String, parameter
           "query" of String, parameter "sort_by" of list of type
           "column_sorting" -> tuple of size 2: parameter "column" of String,
           parameter "ascending" of type "boolean" (Indicates true or false
           values, false = 0, true = 1 @range [0,1]), parameter "start" of
           Long, parameter "limit" of Long, parameter "num_found" of Long
        :returns: instance of type "SearchComparisonGenomesFromCGResult"
           (num_found - number of all items found in query search (with only
           part of it returned in "comparison genomes" list).) -> structure:
           parameter "query" of String, parameter "start" of Long, parameter
           "comparison_genomes" of list of type "GenomeComparisonGenome"
           (GenomeComparisonGenome object: this object holds information
           about a genome in a genome comparison) -> structure: parameter
           "id" of String, parameter "genome_ref" of type "Genome_ref",
           parameter "genome_similarity" of mapping from String to tuple of
           size 2: Long, Long, parameter "name" of String, parameter
           "taxonomy" of String, parameter "features" of Long, parameter
           "families" of Long, parameter "functions" of Long, parameter
           "num_found" of Long
        """
        return self._client.call_method(
            'PanGenomeAPI.search_comparison_genome_from_comparison_genome',
            [params], self._service_ver, context)

    def compute_summary_from_pangenome(self, params, context=None):
        """
        :param params: instance of type "ComputeSummaryFromPG" -> structure:
           parameter "pangenome_ref" of String
        :returns: instance of type "ComputeSummaryFromPGResult" -> structure:
           parameter "families" of mapping from String to Long, parameter
           "genes" of mapping from String to Long, parameter
           "shared_family_map" of mapping from String to mapping from String
           to Long, parameter "genome_ref_name_map" of mapping from String to
           mapping from String to String, parameter "pangenome_id" of String,
           parameter "genomes" of Long
        """
        return self._client.call_method(
            'PanGenomeAPI.compute_summary_from_pangenome',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('PanGenomeAPI.status',
                                        [], self._service_ver, context)
